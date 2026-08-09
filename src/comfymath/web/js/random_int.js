import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "ComfyMathNG.IntRandomNumber",
    async beforeRegisterNodeDef(nodeType, nodeData) {
        if (nodeData.name !== "CM_IntRandomNumber") {
            return;
        }

        const onExecuted = nodeType.prototype.onExecuted;
        nodeType.prototype.onExecuted = function (message) {
            onExecuted?.apply(this, arguments);

            const value = message?.value?.[0];
            const widget = this.widgets?.find((item) => item.name === "value");
            if (widget === undefined || value === undefined) {
                return;
            }

            widget.value = value;
            widget.callback?.(value);
            app.graph?.setDirtyCanvas(true, true);
        };
    },
});
